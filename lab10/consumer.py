from kafka import KafkaConsumer, KafkaProducer
import json
from collections import Counter
import psycopg2

# Подключение к PostgreSQL
conn = psycopg2.connect(
    dbname="kafka_messages",
    user="postgres",
    password="123456",  # замените на ваш пароль
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Kafka Consumer
consumer = KafkaConsumer(
    'user_actions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='my_consumer_group',
    auto_offset_reset='earliest'
)

# Kafka Producer для DLT
dlt_producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

action_counter = Counter()

print("Консьюмер запущен. Ожидаем сообщения...")

for message in consumer:
    data = message.value
    try:
        # Проверка данных
        if not all(k in data for k in ("user_id", "action", "timestamp")):
            raise ValueError("Некорректное сообщение: отсутствуют поля")

        # Фильтрация: только "purchase"
        if data['action'] == 'purchase':
            print("Покупка:", data)
            action_counter[data['action']] += 1
            print("Статистика:", dict(action_counter))

            # Сохраняем в PostgreSQL
            cur.execute(
                "INSERT INTO user_actions (user_id, action, timestamp) VALUES (%s, %s, %s)",
                (data["user_id"], data["action"], data["timestamp"])
            )
            conn.commit()
        else:
            print("Пропущено (не purchase):", data)

    except Exception as e:
        print("Ошибка при обработке сообщения:", e)
        print("Отправка в DLT...")
        dlt_producer.send('user_actions_dlt', data)
        dlt_producer.flush()



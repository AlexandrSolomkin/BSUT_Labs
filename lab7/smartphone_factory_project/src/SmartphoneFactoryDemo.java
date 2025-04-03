public class SmartphoneFactoryDemo {
    public static void main(String[] args) {
        // Создаем фабрики для разных типов смартфонов
        SmartphoneFactory flagshipFactory = new FlagshipFactory();
        SmartphoneFactory budgetFactory = new BudgetFactory();
        SmartphoneFactory gamingFactory = new GamingFactory();

        // Создаем смартфоны через фабрики
        Smartphone flagship = flagshipFactory.createSmartphone();
        Smartphone budget = budgetFactory.createSmartphone();
        Smartphone gaming = gamingFactory.createSmartphone();

        // Выводим характеристики смартфонов
        System.out.println("Flagship Smartphone:\n" + flagship.getSpecifications());
        System.out.println("\nBudget Smartphone:\n" + budget.getSpecifications());
        System.out.println("\nGaming Smartphone:\n" + gaming.getSpecifications());
    }
}

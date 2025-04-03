public class GamingFactory extends SmartphoneFactory {
    @Override
    public Smartphone createSmartphone() {
        return new GamingSmartphone();
    }
}

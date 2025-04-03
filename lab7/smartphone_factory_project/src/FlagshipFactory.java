public class FlagshipFactory extends SmartphoneFactory {
    @Override
    public Smartphone createSmartphone() {
        return new FlagshipSmartphone();
    }
}

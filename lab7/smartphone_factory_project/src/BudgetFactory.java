public class BudgetFactory extends SmartphoneFactory {
    @Override
    public Smartphone createSmartphone() {
        return new BudgetSmartphone();
    }
}

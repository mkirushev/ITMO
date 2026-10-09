package Move;

import ru.ifmo.se.pokemon.*;

final public class HydroPump extends SpecialMove {
    public HydroPump() {
        super(Type.WATER, 110, 0.8);
    }

    @Override
    public String describe() {
        return "uses ability \"Hydro Pump\"";
    }     
}

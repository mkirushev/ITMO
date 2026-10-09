package Move;

import ru.ifmo.se.pokemon.*;

final public class Venoshock extends SpecialMove{
    public Venoshock() {
        super(Type.POISON, 65, 1);
    }

    @Override 
    protected double calcBaseDamage(Pokemon att, Pokemon def) {
        double dmg = super.calcBaseDamage(att, def);

        if (def.getCondition() == Status.POISON) {
            dmg *= 2;
        }

        return dmg;
    }

    @Override
    public String describe() {
        return "uses ability \"Venoshock\"";
    }

}

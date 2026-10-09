package Move;

import ru.ifmo.se.pokemon.*;

final public class SuperFang extends PhysicalMove{
    public SuperFang() {
        super(Type.NORMAL, 0, 0.9);
    }

    @Override 
    protected double calcBaseDamage(Pokemon att, Pokemon def) {
        return def.getHP() / 2;
    }

    @Override
    public String describe() {
        return "uses ability \"Super Fang\"";
    }
}

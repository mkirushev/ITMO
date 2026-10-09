package Move;

import ru.ifmo.se.pokemon.*;

final public class DragonBreath extends SpecialMove {
    public DragonBreath() {
        super(Type.DRAGON, 60, 100);
    }

    @Override 
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() <= 0.3) {
            Effect.paralyze(p);
        }
    }

    @Override
    public String describe() {
        return "uses ability \"Dragon Breath\"";
    }
}

package Move;

import ru.ifmo.se.pokemon.*;

final public class StunSpore extends StatusMove {
    public StunSpore() {
        super(Type.GRASS, 0, 0.75);
    }

    @Override 
    protected void applyOppEffects(Pokemon p) {
        Effect.paralyze(p);
    }

    @Override
    public String describe() {
        return "uses ability \"Stun Spore\"";
    }
}
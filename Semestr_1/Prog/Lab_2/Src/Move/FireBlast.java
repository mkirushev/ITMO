package Move;

import ru.ifmo.se.pokemon.*;

final public class FireBlast extends SpecialMove {
    public FireBlast() {
        super(Type.FIRE, 110, 0.85);
    }

    @Override 
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() <= 0.1) {
            Effect.burn(p);
        }
    }   

    @Override
    public String describe() {
        return "uses ability \"Fire Blast\"";
    } 
}

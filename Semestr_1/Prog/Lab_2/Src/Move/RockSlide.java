package Move;

import ru.ifmo.se.pokemon.*;

final public class RockSlide extends PhysicalMove {
    public RockSlide() {
        super(Type.ROCK, 75, 0.9);
    }

    @Override 
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() <= 0.3) {
            Effect.flinch(p);
        }
    }   

    @Override
    public String describe() {
        return "uses ability \"Rock Slide\"";
    }
}

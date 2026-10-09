package Move;

import ru.ifmo.se.pokemon.*;;

final public class LeafTornado extends SpecialMove {
    public LeafTornado() {
        super(Type.GRASS, 65, 0.9);
    }

    @Override 
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() <= 0.3) {
            p.addEffect(new Effect().stat(Stat.ACCURACY, -1));
        }
    }

    @Override
    public String describe() {
        return "uses ability \"Leaf Tornado\"";
    }   
}

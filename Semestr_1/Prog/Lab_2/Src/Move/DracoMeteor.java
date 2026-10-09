package Move;

import ru.ifmo.se.pokemon.*;

final public class DracoMeteor extends SpecialMove {
    public DracoMeteor() {
        super(Type.DRAGON, 130, 0.9);
    }

    @Override
    protected void applySelfEffects (Pokemon p) {
        p.addEffect(new Effect().stat(Stat.SPECIAL_ATTACK, -2));
    } 
    
    @Override
    public String describe() {
        return "uses ability \"Draco Meteor\"";
    }
}

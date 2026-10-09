package Move;

import ru.ifmo.se.pokemon.*;

final public class SwordsDance extends StatusMove {
    public SwordsDance() {
        super(Type.NORMAL, 0, 0);
    }

    @Override
    protected void applyOppEffects (Pokemon p) {
        p.addEffect(new Effect().stat(Stat.ATTACK, 2));
    }   

    @Override
    public String describe() {
        return "uses ability \"Swords Dance\"";
    }
}

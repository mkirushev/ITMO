package Move;

import ru.ifmo.se.pokemon.*;

final public class SweetScent extends StatusMove {
    public SweetScent() {
        super(Type.NORMAL, 0, 1);
    }

    @Override
    protected void applyOppEffects (Pokemon p) {
        p.addEffect(new Effect().stat(Stat.EVASION, -1));
    }

    @Override
    public String describe() {
        return "uses ability \"Sweet Scene\"";
    }
}

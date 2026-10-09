package Move;

import ru.ifmo.se.pokemon.*;

final public class Swagger extends StatusMove{
    public Swagger() {
        super(Type.NORMAL, 0, 0.85);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        p.confuse();
        p.addEffect(new Effect().stat(Stat.ATTACK, 2));
    }

    @Override
    public String describe() {
        return "uses ability \"Swagger\"";
    }
}

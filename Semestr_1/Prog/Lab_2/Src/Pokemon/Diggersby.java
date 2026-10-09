package Pokemon;

import ru.ifmo.se.pokemon.*;
import Move.*;

final public class Diggersby extends Bunnelby {
    public Diggersby(String name, int level) {
        super(name, level);
        this.setType(Type.NORMAL);
        this.setStats(85, 56, 77, 50, 77, 78);
        this.setMove(
            new SwordsDance()
        );
    }
}
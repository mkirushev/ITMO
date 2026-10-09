package Pokemon;

import ru.ifmo.se.pokemon.*;
import Move.*;

final public class Victreebel extends Weepinbell {
    public Victreebel(String name, int level) {
        super(name, level);
        this.setType(Type.GRASS);
        this.setStats(80, 105, 65, 100, 70, 70);
        this.setMove(
            new LeafTornado()
        );
    }
}
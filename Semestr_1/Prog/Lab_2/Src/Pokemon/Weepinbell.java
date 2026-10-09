package Pokemon;

import ru.ifmo.se.pokemon.*;
import Move.*;

public class Weepinbell extends Bellsprout {
    public Weepinbell(String name, int level) {
        super(name, level);
        this.setType(Type.GRASS);
        this.setStats(65, 90, 50, 85, 45, 55);
        this.setMove(
            new StunSpore()
        );
    }
}
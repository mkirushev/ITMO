package Pokemon;

import ru.ifmo.se.pokemon.*;
import Move.*;

public class Bellsprout extends Pokemon {
    public Bellsprout(String name, int level) {
        super(name, level);
        this.setType(Type.GRASS);
        this.setStats(50, 75, 35, 70, 30, 40);
        this.setMove(
            new Venoshock(),
            new SweetScent()
        );
    }
}
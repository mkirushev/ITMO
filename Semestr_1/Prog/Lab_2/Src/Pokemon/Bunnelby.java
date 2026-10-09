package Pokemon;

import ru.ifmo.se.pokemon.*;
import Move.*;

public class Bunnelby extends Pokemon {
    public Bunnelby(String name, int level) {
        super(name, level);
        this.setType(Type.NORMAL);
        this.setStats(38, 36, 38, 32, 36, 57);
        this.setMove(
            new RockSlide(),
            new SuperFang(),
            new Swagger()
        );
    }
}
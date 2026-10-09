package Pokemon;

import ru.ifmo.se.pokemon.*;
import Move.*;

public class Palkia extends Pokemon {
    public Palkia(String name, int level) {
        super(name, level);
        this.setType(Type.WATER);
        this.setStats(90, 120, 100, 150, 120, 100);
        this.setMove(
            new DracoMeteor(),
            new FireBlast(),
            new HydroPump(),
            new DragonBreath()
        );
    }
}
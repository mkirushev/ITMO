import ru.ifmo.se.pokemon.*;
import Pokemon.*;

public class Main {
    public static void main(String[] args) {
        Battle battle = new Battle();

        Pokemon bellsprout = new Bellsprout("Bellsprout", 1);
        Pokemon Weepinbell = new Weepinbell("Weepinbell", 1);
        Pokemon Victreebel = new Victreebel("Victreebel", 1);
        Pokemon bunnelby = new Bunnelby("Bunnelby", 1);
        Pokemon diggersby = new Diggersby("Diggersby", 1);
        Pokemon palkia = new Palkia("Palkia", 1);

        battle.addAlly(bellsprout);
        battle.addAlly(Weepinbell);
        battle.addAlly(Victreebel);
        battle.addFoe(bunnelby);
        battle.addFoe(diggersby);
        battle.addFoe(palkia);
        
        battle.go();
    }
}
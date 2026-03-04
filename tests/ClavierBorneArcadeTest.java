import static org.junit.Assert.*;
import org.junit.Test;

public class ClavierBorneArcadeTest {

    @Test
    public void defaultStateIsFalse() {
        ClavierBorneArcade k = new ClavierBorneArcade();
        assertFalse(k.getJoyJ1GaucheEnfoncee());
        assertFalse(k.getJoyJ1DroiteEnfoncee());
        assertFalse(k.getJoyJ1HautEnfoncee());
        assertFalse(k.getJoyJ1BasEnfoncee());
        assertFalse(k.getBoutonJ1AEnfoncee());
        assertFalse(k.getBoutonJ1ZEnfoncee());
        assertFalse(k.getJoyJ1GaucheTape());
        assertFalse(k.getJoyJ1DroiteTape());
    }

    @Test
    public void tapeGettersReset() {
        ClavierBorneArcade k = new ClavierBorneArcade();
        k.getJoyJ1GaucheTape();
        assertFalse(k.getJoyJ1GaucheTape());
    }
}

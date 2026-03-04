import static org.junit.Assert.*;
import org.junit.Test;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class HighScoreTest {

    @Test
    public void suivantPrecedent_Bordures() {
        assertEquals('B', HighScore.suivant('A'));
        assertEquals('Z', HighScore.suivant('Y'));
        assertEquals('.', HighScore.suivant('Z'));
        assertEquals(' ', HighScore.suivant('.'));
        assertEquals('A', HighScore.suivant(' '));

        assertEquals('A', HighScore.precedent('B'));
        assertEquals(' ', HighScore.precedent('A'));
        assertEquals('.', HighScore.precedent(' '));
        assertEquals('Z', HighScore.precedent('.'));
    }

    @Test
    public void fichier_LectureEcriture() throws IOException {
        File temp = File.createTempFile("hs", ".hig");
        temp.deleteOnExit();

        ArrayList<LigneHighScore> list = new ArrayList<>();
        list.add(new LigneHighScore("ABC", 123));
        HighScore.enregistrerFichier(temp.getPath(), list, "ABC", 123);
        ArrayList<LigneHighScore> lu = HighScore.lireFichier(temp.getPath());
        assertEquals(1, lu.size());
        assertEquals(123, lu.get(0).getScore());
        assertEquals("ABC", lu.get(0).getNom());
    }
}

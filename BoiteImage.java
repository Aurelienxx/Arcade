import java.io.File;

import MG2D.geometrie.Point;
import MG2D.geometrie.Rectangle;
import MG2D.geometrie.Texture;


public class BoiteImage extends Boite{

    Texture image;

    BoiteImage(Rectangle rectangle, String chemin) {
        super(rectangle);
        String full_path = chemin+"/photo_small.png";
        this.image = new Texture(full_path, new Point(760, 648));
    }

    public Texture getImage() {
	    return this.image;
    }

    public void setImage(String chemin) {
        String full_path = chemin+"/photo_small.png";
        this.image.setImg(full_path);
        //this.image.setTaille(400, 320);
    }

}

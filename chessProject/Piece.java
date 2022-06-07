/* abstract class for pieces. includes all the attributes of a piece needed. specific manuverability of pieces will be defined in their individual classes that extend this abstract class */
public abstract class Piece{
    private boolean captured = false;
    private int value;
    private boolean white = false;

    public Piece(boolean captured,int value, boolean white) {
        this.captured = captured;
        this.value = value;
        this.white = white;
    }

    public boolean isWhite() {
        return white;
    }

    public boolean isCaptured() {
        return captured;
    }

    public int getValue() {
        return value;
    }

    public void setWhite(boolean white) {
        this.white = white;
    }

    public void setCaptured(boolean captured) {
        this.captured = captured;
    }

    public abstract boolean canMove(Board board, Spot start, Spot end);
}
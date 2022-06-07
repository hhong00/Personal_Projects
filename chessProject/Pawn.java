public class Pawn extends Piece{

    boolean hasMoved;
    
    public Pawn(boolean captured, boolean white) {
        super(captured, 1, white);
        hasMoved = false;
    }

    public boolean canMove(Board board, Spot start, Spot end) {
        if(end.getPiece().isWhite() == this.isWhite()) {
            return false;
        }

        int x = end.returnX() - start.returnX();
        int y = end.returnY() - start.returnY();

        /* case if white piece moves up one move */
        if(this.isWhite() && x == -1 && y == 0 && !end.getPiece().isWhite()) 
            return true;
        /* case if black piece moves down one move */
        else if (!this.isWhite() && x == 1 && y == 0 && end.getPiece().isWhite()) 
            return true;
        /* case if white piece moves up twice on first move */
        else if (this.isWhite() && x == -2 && y == 0 && !hasMoved)
            return true;
        /* case if black piece moves down twice on first move */
        else if (!this.isWhite() && x == 2 && y == 0 && !hasMoved) 
            return true;
        /* case if white piece diagonally captures black piece */
        else if (this.isWhite() && !end.getPiece().isWhite() && x == -1 && Math.abs(y) == 1)
            return true;
        /* case if black piece diagonally captures white piece */
        else if (!this.isWhite() && end.getPiece().isWhite() && x == 1 && Math.abs(y) == 1)
            return true;
        /* all other cases */
        else
            return false;
    }

    public void setHasMoved(boolean hasMoved) {
        this.hasMoved = hasMoved;
    }


}

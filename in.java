public class Fun {
    Fun() {
        System.out.println("Fun constructor");
    }
    void fun() {
        System.out.println("Fun mathod");
    }
    public static void main(String[] args) {
        Fun fu = new Fun();
        fu.fun();
        Fen fe = new Fen();
        fe.fen();
        Fin fi = new Fin();
        fi.fin();
        Fon fo = new Fon();
        fo.fon();
        Fan fa = new Fan();
        fa.fan();
        fa.run();
    }
}

class Fen {
    Fen() {
        System.out.println("fen construuctor");

    }
    void fen() {
        System.out.println("Fen method");
    }
}

class Fin {
    void fin() {
        System.out.println("Fin method");
    }
}

class Fon {
    void fon() {
        System.out.println("Fon method");
    }
}

class Fan {
    void fan() {
        System.out.println("Fan method");
    }
    public void run() {
        System.out.println("run");
    }
}

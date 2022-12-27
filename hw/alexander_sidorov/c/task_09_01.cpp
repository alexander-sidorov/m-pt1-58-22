#include <iostream>

class Function {
public:
    virtual void operator()() = 0;
};


class Helloworld: public Function {
public:
    void operator() () {
        std::cout << "Hello world!" << std::endl;
    }
};

class DoTwice: public Function {
    Function* const _inner;

public:
    explicit DoTwice(Function* const inner) : _inner(inner) {}

    void operator()() {
        (*_inner)();
        (*_inner)();
    }
};


int main() {
    Function* helloworld = new Helloworld();
    helloworld = new DoTwice(helloworld);

    (*helloworld)();
}

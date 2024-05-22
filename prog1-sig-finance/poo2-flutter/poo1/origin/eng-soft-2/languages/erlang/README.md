# Erlang - Exemplos

[Hello World](https://erlangbyexample.org/hello-world)

## Source Code

```erlang
-module(hello_world).
-compile(export_all).

hello() ->
    io:format("hello world~n").
```

## Compile and Run

```bash
$ ls
hello_world.erl

$ erl
Eshell (abort with ^G)

1> c(hello_world).
2> hello_world:hello().
hello world
ok
```
package br.ufrn.bsi.webflux.model;

import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "devs")
public class Devs {

    private String id;

    private String name;

    private String stack;

    public Devs() {
    }

    public Devs(String id, String name, String stack) {
        this.id = id;
        this.name = name;
        this.stack = stack;
    }    

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getStack() {
        return stack;
    }

    public void setStack(String stack) {
        this.stack = stack;
    }
    
}

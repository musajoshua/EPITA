package fr.epita.datamodel;

public class Person {
    private String name;
    private String pClass;
    private Double age;
    private String sex;
    private Integer survived;

    public Person(String name, String pClass, Double age, String sex, Integer survived) {
        this.name = name;
        this.pClass = pClass;
        this.age = age;
        this.sex = sex;
        this.survived = survived;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getpClass() {
        return pClass;
    }

    public void setpClass(String pClass) {
        this.pClass = pClass;
    }

    public Double getAge() {
        return age;
    }

    public void setAge(Double age) {
        this.age = age;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public Integer getSurvived() {
        return survived;
    }

    public void setSurvived(Integer survived) {
        this.survived = survived;
    }
}

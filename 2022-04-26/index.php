<?php

class Person
{
    protected string $firstName;
    protected string $lastName;

    function __construct(string $firstName, string $lastName)
    {
        $this->name = $firstName;
        $this->lastName = $lastName;
    }
}

// $oject = new FullName("Satyarath", "Sharma");

class Student extends Person
{
    function studentName(): void
    {
        echo "I am a student. My name is {$this->firstName} {$this->lastName}";
    }
}


$object = new Person("Satyarath", "Sharma");
$object2->studentName();




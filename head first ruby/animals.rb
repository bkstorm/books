class Dog

    attr_accessor :name, :age

    def talk 
        puts "#{@name} says Bark!"
    end

    def move(destination)
        puts "#{@name} runs to the #{destination}."
    end

    def report_age
        puts "#{@name} is #{@age} years old."
    end
end

class Bird
    def talk
        puts "Chirp! Chirp!"
    end

    def move(destination)
        puts "Flying to the #{destination}."
    end
end

class Cat
    def talk
        puts "Meow!"
    end

    def move(destination)
        puts "Running to the #{destination}."
    end
end

fido = Dog.new
fido.name = "Fido"
fido.age = 2
rex = Dog.new
rex.name = "Rex"
rex.age = 3
fido.report_age
rex.report_age
class Vehicle
    attr_accessor :odometer
    attr_accessor :gas_used

    def accelerate
        puts "Floor it!"
    end

    def sound_horn
        puts "Beep! Beep!"
    end

    def steer
        puts "Turn front 2 wheels."
    end

    def mileage
        return @odometer / @gas_used
    end

end
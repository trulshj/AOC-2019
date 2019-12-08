
file = File.open("input.txt")
masses = file.readlines.map { |mass| mass.chomp.to_i }
file.close

def get_fuel(mass)
  mass / 3 - 2
end

part1 = masses.reduce(0) { |sum, mass| sum + get_fuel(mass)}

fuel_requierment = 0
masses.each do |mass|
  fuel = get_fuel(mass)
  while fuel > 0
    fuel_requierment += fuel
    fuel = get_fuel(fuel)
  end
end

part2 = fuel_requierment

puts " Day 1 ".center(64, '-')
puts "Fuel requierment: #{part1}".center(64)
puts "Fuel requierment accounting for mass of fuel: #{part2}".center(64)
puts "".center(64, '-')

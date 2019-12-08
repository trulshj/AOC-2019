
require 'set'
start, stop = 197487, 673251
start_time = Process.clock_gettime(Process::CLOCK_MONOTONIC)

def check1(n)
  n = n.to_s.chars
  if n != n.sort or n.to_set.size == n.size
    return false
  end
  return true
end


def check2(n)
  n = n.to_s.chars
  counts = n.map { |d| n.to_s.count(d) }
  counts.include? 2
end


part1, part2 = 0, 0

(start..stop).each do |n|
  if check1(n)
    part1 += 1
    if check2(n)
      part2 += 1
    end
  end
end

end_time = Process.clock_gettime(Process::CLOCK_MONOTONIC)

puts ""
puts " Day 4 ".center(64, '-') + "\n"
puts ""

x = start
(start..stop).step(10) do |n|
  x += 10.0
  print ("Checking: #{n} - #{(100*(x/stop)).round}% done...".center(64)) + "\r"
  if x >= stop
    sleep 0.3
    puts "Checking: #{n} - #{(100*(x/stop)).round}% done...".center(64)
    puts "Checked #{stop-start} passwords - 100% done".center(64)
    puts ""
  end
end

sleep 0.5
(0..part1).each do |i|
  print ("Passwords with lax criteria: #{i}".center(64)) + "\r"
  sleep 0.0005
end
puts "Passwords with lax criteria: #{part1}".center(64)
sleep 0.5
(0..part2).each do |i|
  print ("Passwords with strict criteria: #{i}".center(64)) + "\r"
  sleep 0.0005
end
puts "Passwords with strict criteria: #{part2}".center(64)
puts ""
sleep 0.5
puts "Actually found in #{(end_time - start_time).round(7)} seconds".center(64)
puts "".center(64, '-')

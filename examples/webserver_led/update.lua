sv:listen(80, function(c)
    c:on("receive", function(c, p)
        -- toggle led
        if string.match(p, '\\?led=on') then
            gpio.write(led, gpio.HIGH)
        elseif string.match(p, '\\?led=off') then
            gpio.write(led, gpio.HIGH)
        else
            -- send html to client
            c:send(read_file("index.html"))
        end
        c:close()
    end)
end)

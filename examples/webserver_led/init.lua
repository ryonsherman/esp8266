LED = 4 -- GPIO2
gpio.mode(LED, gpio.OUTPUT)

-- file read helper
function read_file(f)
    file.open(f)
    data = ""
    line = file.readline()
    while line do
        data = data .. line
        line = file.readline()
    end
    file.close()
    return data
end

-- set wifi ap mode
wifi.setmode(wifi.SOFTAP)

-- configure wifi ap
cfg = {}
cfg.ssid = "esp8266"
cfg.pwd  = "esp8266pwd"
wifi.ap.config(cfg)

-- create web server
sv = net.createServer(net.TCP, 30)
sv:listen(80, function(c)
    c:on("receive", function(c, p)
        -- toggle led
        if string.match(p, '\\?led=on') then
            gpio.write(LED, gpio.HIGH)
        elseif string.match(p, '\\?led=off') then
            gpio.write(LED, gpio.LOW)
        -- send html to client
        else
            c:send(read_file("index.html"))
        end
        c:close()
    end)
end)

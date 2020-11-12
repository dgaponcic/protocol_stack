class SocketWrapper:
  def __init__(self, sock, connection):
    self.sock = sock
    self.connection = connection
  
  def fileno(self):
    return self.sock.fileno()

  def recvfrom(self, buffer):
    return self.sock.recvfrom(buffer)

  def sendto(self, msg, addr):
    self.sock.sendto(msg, addr)
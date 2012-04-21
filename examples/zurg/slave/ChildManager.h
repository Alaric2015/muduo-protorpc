#ifndef MUDUO_PROTORPC_ZURG_CHILDMANAGER_H
#define MUDUO_PROTORPC_ZURG_CHILDMANAGER_H

#include <muduo/net/Channel.h>

#include <boost/noncopyable.hpp>
#include <boost/function.hpp>

#include <map>

namespace muduo
{
namespace net
{
class EventLoop;
}
}

struct rusage;

namespace zurg
{

class ChildManager : boost::noncopyable
{
 public:
  typedef boost::function<void(int status, const struct rusage&)> Callback;

  explicit ChildManager(muduo::net::EventLoop* loop);
  ~ChildManager();

  void start();

  void runAtExit(pid_t pid, const Callback&);

 private:
  void onRead(muduo::Timestamp t);

  muduo::net::EventLoop* loop_;
  int signalFd_;
  muduo::net::Channel channel_;
  std::map<pid_t, Callback> callbacks_;
};

}

#endif  // MUDUO_PROTORPC_ZURG_CHILDMANAGER_H

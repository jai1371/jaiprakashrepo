from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from .models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete,post_init,pre_init
from django.core.signals import request_started,request_finished,got_request_exception

'''max_login=3
@receiver(user_logged_in,sender=User)
def login_success(sender,request,**kwargs):
    max_login=3
    print("login")
    print("sender:",sender)
    print("request:",request)
    print("user:",User)
    print(f"kwargs:{kwargs}")

# user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out,sender=User)
def logout_success(sender,request,**kwargs):
    max_login=3
    print("logout")
    print(max_login)
    print("sender:",sender)
    print("request:",request)
    print("user:",User)
    print(f"kwargs:{kwargs}")

@receiver(user_login_failed)
def login_failed(sender,request,**kwargs):
    global max_login
    max_login-=1
    if max_login==0:
        print("your are failed to login")
    print("loginfailed")
    print(max_login)
    print("sender:",sender)
    print("request:",request)
    print("user:",User)
    print(f"kwargs:{kwargs}")


@receiver(pre_save,sender=User)
def pre_save_before_created(sender,instance,**kwargs):
    print("pre save")
    print("sender:",sender)
    print("instance:",instance)
    print("user:",User)
    print(f"kwargs:{kwargs}")

@receiver(post_save,sender=User)
def post_save_after_created(sender,instance,created,**kwargs):
    if created:
        print("post save created")
        print("sender:",sender)
        print("instance:",instance)
        print("user:",User)
        print(f"kwargs:{kwargs}")
    else:
        print("post save updated")
        print("sender:", sender)
        print("instance:", instance)
        print("user:", User)
        print(f"kwargs:{kwargs}")

@receiver(pre_delete,sender=User)
def pre_delete_user(sender,instance,**kwargs):
    print("before deleted")
    print("sender:",sender)
    print("request:",instance)
    print("user:",User)
    print(f"kwargs:{kwargs}")

@receiver(post_delete,sender=User)
def post_delete_user(sender,instance,**kwargs):
    print("after deleted")
    print("sender:",sender)
    print("request:",instance)
    print("user:",User)
    print(f"kwargs:{kwargs}")

@receiver(request_started)
def request_start(sender,environ,**kwargs):
    print("request_start")
    print("user:",User)
    print(f"kwargs:{kwargs}")

@receiver(request_finished)
def request_finish(sender,**kwargs):
    print("request_finish")
    print("user:",User)
    print(f"kwargs:{kwargs}")

@receiver(got_request_exception)
def got_exception(sender,request,**kwargs):
    print("got exception")
    print("user:",User)
    print(f"kwargs:{kwargs}")
'''
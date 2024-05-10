# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# import redis
# from django.conf import settings
# from django.utils.crypto import get_random_string
#
# # Connect to Redis
# redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
#
# # Function to generate activation code
#
#
# class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return (
#                 str(user.is_active) + str(user.pk) + str(timestamp)
#         )
#
#
# email_verification_token = EmailVerificationTokenGenerator()
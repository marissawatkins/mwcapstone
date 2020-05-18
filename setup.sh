export DATABASE_URL='postgres://postgres@localhost:5432/capstone'
export SQLALCHEMY_TRACK_MODIFICATIONS=False
export AUTH0_DOMAIN="mwcapstone.auth0.com"
export API_AUDIENCE='capstone'
export ALGORITHMS=['RS256']
export PRODUCER_JWT="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZkMC1Dc3JzQWJkcG1qQzVOZmo3dSJ9.eyJpc3MiOiJodHRwczovL213Y2Fwc3RvbmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzJkZWE2NmEzMDU0MGNkOTg0ZGU0MiIsImF1ZCI6Im13Y2Fwc3RvbmUiLCJpYXQiOjE1ODk4NDE2NTIsImV4cCI6MTU4OTg0ODg1MiwiYXpwIjoibUpMZ25xdERpdzFnbHk2cXBsOFNjQjE3ZmlKNXdJTGgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.f9I1x0BXRUt5qkozLTZljl6nppXhZNcWprwS5Gm8W7yjmsNBCJrqsKoGnHnWBOjuQQXa5tIcwmMmv5c8X5NjNNe9-Egzk9lzFN9GnhHp6ltInoNP0jbxB95N_5FclNTfi0SRFeJSEsfKgjDDuD5lg2yPc_jMJBrEtibuseU6smLu3jdCU39ua7_BDSwjEdU-VE1Mv_XKWe5w4AuegoFP34uXw16jfxvKux5TjlAAXJNoLr95s0WT0ThqgcidrbtllXEjgFe8-W02sasjZwdXKAnviacuTnOOUdNj_d4ksAEBEsprJ_RsejKSXflkC0BcFtGEohDm7gCxcl9HhMw9lA&expires_in=7200&token_type=Bearer"
export DIRECTOR_JWT="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZkMC1Dc3JzQWJkcG1qQzVOZmo3dSJ9.eyJpc3MiOiJodHRwczovL213Y2Fwc3RvbmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzJkZTdjOWMwN2ExMGNlN2M3MmI1NSIsImF1ZCI6Im13Y2Fwc3RvbmUiLCJpYXQiOjE1ODk4NDE0MTgsImV4cCI6MTU4OTg0ODYxOCwiYXpwIjoibUpMZ25xdERpdzFnbHk2cXBsOFNjQjE3ZmlKNXdJTGgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.ZDSa_MzTzU3_kbMd9veJHU1mIRdIcIps0t9JpIp-qsoUY2b8blxsctuy8USC1_gBVSzlKJfWJzZqLaKpXMHiWxGmcCVyKMswveCmZyWvkbaIBwty0x8sfAHDfeOKmII5qxd24yuNuOn2JL8l74Ct9zTiCG7F_5y53ApjiDrxNrmSAwj-rywpRTSc4nIUuaD9DUdJRc368q9_fQxVjbDdrUwwe1otTKi7SMRqfjpg2NmF6EGq0WV_Hn8RB69nArcJK5EYS-DtsZNV8yaJbz3SWr2pltLgLFrCw5Ltfi1T4DZiZCw9q6Jy53CNf6DI9x-PspE-XdHYJjcEQUjnQjbMnw&expires_in=7200&token_type=Bearer"
export ASSISTANT_JWT="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZkMC1Dc3JzQWJkcG1qQzVOZmo3dSJ9.eyJpc3MiOiJodHRwczovL213Y2Fwc3RvbmUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzJkZTM5OWMwN2ExMGNlN2M3MjlmNSIsImF1ZCI6Im13Y2Fwc3RvbmUiLCJpYXQiOjE1ODk4NDEyNjksImV4cCI6MTU4OTg0ODQ2OSwiYXpwIjoibUpMZ25xdERpdzFnbHk2cXBsOFNjQjE3ZmlKNXdJTGgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.EWUxAYkMGWhbQC-7XOTcTUYvCJhTDxXNhAEUMsYkBrH1FDWV9maiIpO8v7ePCtYwcBm15DDwY0QWaR6jDP0guAom0Cor3nNIXG7nxHMgUZdL47wz3CBQeBeFlPzGNWXqFq4_CCjuAe5YXD7O11yyr-zUKMQ2cGr9HWOexrmjtho29V3cO3H6VhYjoUWaf7LKChcGd0ffoEkqtQQ22Wa4FZ91Askc3_sf_rp26rLsTACe9ETlR-G2sWZyvF8QihSCA5LV4eWxBwSL_H7mrpxTGhWgHkDGDZYG6VAepmKsfu8_uKAGBZ3blwQR54AtMX7Z5pocFTujoO45AF_usqsj0Q&expires_in=7200&token_type=Bearer"
export CLIENT_ID='mJLgnqtDiw1gly6qpl8ScB17fiJ5wILh'
LOG_LEVEL=DEBUG


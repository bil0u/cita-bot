# Troubleshooting

For Windows, escape paths with additional backslash, e.g. `C:\\Users\\lehne`

If you feel like the script is being stuck at the office selection page — it's not, it refreshes the page 12 times (maximum allowed) until the office is found and then starts over.

`SMTH BROKEN: [Errno 13]` — that means the script is unable to write a file to file system, try to adjust permissions for it, or set `save_artifacts=False` to disable saving snapshots for offices/appointments.

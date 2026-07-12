Store it in **GitHub → SSH keys** (not inside your repository).

Steps:

1. Open GitHub in your browser.
2. Click your **profile picture** (top-right).
3. Go to:

```
Settings
   ↓
SSH and GPG keys
   ↓
New SSH key
```

4. Fill in:

**Title:**
Something that identifies the computer, for example:

```
Laptop Linux
```

or

```
Nkandi laptop
```

**Key type:**
Leave as:

```
Authentication Key
```

**Key:**
Paste the output from your terminal:

```bash
cat ~/.ssh/id_ed25519.pub
```

It should look like:

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... your_email
```

5. Click:

```
Add SSH key
```

---

After adding it, go back to your terminal and test:

```bash
ssh -T git@github.com
```

You should see something like:

```
Hi r13t0! You've successfully authenticated, but GitHub does not provide shell access.
```

Then change your project from HTTPS to SSH:

```bash
cd ~/pylearn
git remote set-url origin git@github.com:r13t0/pylearn.git
```

Check:

```bash
git remote -v
```

Then:

```bash
git push
```

From now on:

* Laptop → `git push` → GitHub
* Other devices → `git pull` → get updates

Your Git workflow will be properly connected.


=============================================================


If the folders are **empty**, then you have found the reason.

Git does **not track empty folders**.

So this:

```text
pylearn/
├── Patterns/
└── Pipelines/
```

exists on your computer, but Git sees nothing to upload because there are no files inside.

Git only tracks **files**, not folders.

---

## Solution: add placeholder files

Inside your computer:

```bash
cd ~/pylearn
```

Create placeholder files:

```bash
touch Patterns/.gitkeep
touch Pipelines/.gitkeep
```

Now Git sees files:

```text
Patterns/
└── .gitkeep

Pipelines/
└── .gitkeep
```

Then upload:

```bash
git add .
git commit -m "Add Patterns and Pipelines folders"
git push
```

On Android:

```bash
git pull
```

Now the folders will appear.

---

The `.gitkeep` file is just a convention. It tells Git:

> "Keep this folder structure even though it is currently empty."

Later, when you add real files:

```text
Patterns/
├── sequence.md
├── iteration.md
└── selection.md
```

you can delete `.gitkeep` if you want.



#!/usr/bin/env node

/**
 * Interactive CLI Menu for MINDCUBBY-3D Repository
 * 
 * Features:
 * - Arrow key navigation
 * - Quick access to common tasks
 * - G-code spec generation
 * - Git operations
 * 
 * Usage: npm run menu
 */

const readline = require('readline');
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

// Get repo root
const repoRoot = execSync('git rev-parse --show-toplevel', { encoding: 'utf-8' }).trim();

// Menu options
const menuItems = [
  { label: '📦 Quick Commit (stage, specs, push)', action: 'quick-commit' },
  { label: '🔍 Generate Specs for Directory', action: 'generate-specs' },
  { label: '📁 Open PRINTABLES Folder', action: 'open-printables' },
  { label: '📊 Git Status', action: 'git-status' },
  { label: '📜 View Recent Commits', action: 'git-log' },
  { label: '🚀 Push Changes', action: 'git-push' },
  { label: '📖 View Setup Guide', action: 'view-setup' },
  { label: '❌ Exit', action: 'exit' },
];

let selectedIndex = 0;

// Create readline interface for key capture
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: true,
});

// Disable line buffering
if (process.stdin.isTTY) {
  process.stdin.setRawMode(true);
}

function clearScreen() {
  console.clear();
}

function displayMenu() {
  clearScreen();
  console.log('\n╔════════════════════════════════════════════╗');
  console.log('║      MINDCUBBY-3D Repository Menu          ║');
  console.log('╚════════════════════════════════════════════╝\n');

  menuItems.forEach((item, index) => {
    const prefix = index === selectedIndex ? '❯ ' : '  ';
    const style = index === selectedIndex ? '\x1b[36m' : '\x1b[0m'; // Cyan highlight
    const reset = '\x1b[0m';
    console.log(`${style}${prefix}${item.label}${reset}`);
  });

  console.log('\n  ↑/↓ Navigate | Enter Select | Q Quit\n');
}

function executeAction(action) {
  clearScreen();

  switch (action) {
    case 'quick-commit': {
      const promptCommitMessage = () => {
        rl.question('📝 Enter commit message: ', (message) => {
          if (!message.trim()) {
            console.log('❌ Commit message cannot be empty');
            setTimeout(showMenu, 1500);
            return;
          }
          try {
            console.log('\n📦 Staging changes...');
            execSync('git add .', { cwd: repoRoot });

            console.log('🔍 Generating specs...');
            execSync(`bash ${repoRoot}/.githooks/pre-commit`, { cwd: repoRoot });

            console.log('💾 Committing...');
            execSync(`git commit -m "${message}"`, { cwd: repoRoot });

            console.log('🚀 Pushing...');
            execSync('git push', { cwd: repoRoot });

            console.log('\n✅ Done!\n');
            setTimeout(showMenu, 2000);
          } catch (error) {
            console.error(`\n❌ Error: ${error.message}\n`);
            setTimeout(showMenu, 2000);
          }
        });
      };
      promptCommitMessage();
      break;
    }

    case 'generate-specs': {
      const promptPath = () => {
        rl.question('📁 Enter directory path (default: PRINTABLES): ', (dir) => {
          const targetDir = dir.trim() || 'PRINTABLES';
          const fullPath = path.join(repoRoot, targetDir);

          if (!fs.existsSync(fullPath)) {
            console.log(`\n❌ Directory not found: ${fullPath}\n`);
            setTimeout(showMenu, 1500);
            return;
          }

          try {
            console.log(`\n🔍 Generating specs for: ${targetDir}\n`);
            execSync(`python3 ${repoRoot}/scripts/gcode_specs.py "${fullPath}"`, {
              cwd: repoRoot,
              stdio: 'inherit',
            });
            console.log('\n✅ Done!\n');
            setTimeout(showMenu, 2000);
          } catch (error) {
            console.error(`\n❌ Error: ${error.message}\n`);
            setTimeout(showMenu, 2000);
          }
        });
      };
      promptPath();
      break;
    }

    case 'open-printables': {
      try {
        const printablesPath = path.join(repoRoot, 'PRINTABLES');
        if (fs.existsSync(printablesPath)) {
          execSync(`open "${printablesPath}"`);
          console.log('📂 Opening PRINTABLES folder...\n');
          setTimeout(showMenu, 1000);
        } else {
          console.log('❌ PRINTABLES folder not found\n');
          setTimeout(showMenu, 1500);
        }
      } catch (error) {
        console.error(`\n❌ Error: ${error.message}\n`);
        setTimeout(showMenu, 1500);
      }
      break;
    }

    case 'git-status': {
      console.log('\n📊 Git Status:\n');
      try {
        execSync('git status', { cwd: repoRoot, stdio: 'inherit' });
        console.log('\n');
        setTimeout(showMenu, 2000);
      } catch (error) {
        console.error(`\n❌ Error: ${error.message}\n`);
        setTimeout(showMenu, 1500);
      }
      break;
    }

    case 'git-log': {
      console.log('\n📜 Recent Commits (last 10):\n');
      try {
        execSync('git log --oneline -10', { cwd: repoRoot, stdio: 'inherit' });
        console.log('\n');
        setTimeout(showMenu, 2000);
      } catch (error) {
        console.error(`\n❌ Error: ${error.message}\n`);
        setTimeout(showMenu, 1500);
      }
      break;
    }

    case 'git-push': {
      console.log('\n🚀 Pushing to remote...\n');
      try {
        execSync('git push', { cwd: repoRoot, stdio: 'inherit' });
        console.log('\n✅ Done!\n');
        setTimeout(showMenu, 1500);
      } catch (error) {
        console.error(`\n❌ Error: ${error.message}\n`);
        setTimeout(showMenu, 1500);
      }
      break;
    }

    case 'view-setup': {
      const setupPath = path.join(repoRoot, 'SETUP_HOOKS.md');
      if (fs.existsSync(setupPath)) {
        try {
          execSync(`less "${setupPath}"`, { stdio: 'inherit' });
        } catch (e) {
          // User exited less
        }
        setTimeout(showMenu, 500);
      } else {
        console.log('❌ SETUP_HOOKS.md not found\n');
        setTimeout(showMenu, 1500);
      }
      break;
    }

    case 'exit': {
      console.log('\n👋 Goodbye!\n');
      process.exit(0);
    }
  }
}

function handleKeyPress(key) {
  if (!key) return;

  const keyCode = key.charCodeAt(0);

  // Arrow up
  if (key === '\x1b[A') {
    selectedIndex = (selectedIndex - 1 + menuItems.length) % menuItems.length;
    displayMenu();
  }
  // Arrow down
  else if (key === '\x1b[B') {
    selectedIndex = (selectedIndex + 1) % menuItems.length;
    displayMenu();
  }
  // Enter
  else if (keyCode === 13) {
    const action = menuItems[selectedIndex].action;
    executeAction(action);
  }
  // Q or q (quit)
  else if (key.toLowerCase() === 'q') {
    executeAction('exit');
  }
}

function showMenu() {
  displayMenu();
}

// Handle input
process.stdin.on('data', (data) => {
  handleKeyPress(data.toString());
});

// Handle exit
process.on('SIGINT', () => {
  console.log('\n\n👋 Goodbye!\n');
  process.exit(0);
});

// Start menu
showMenu();

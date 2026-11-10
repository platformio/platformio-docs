import fs from 'node:fs';
import path from 'node:path';
import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

type SidebarItemConfig = Extract<SidebarsConfig[string], unknown[]>[number];

const DOCS_DIR = path.join(__dirname, 'docs');

/** A category whose landing page is `<dir>/index`. */
function section(
  label: string,
  dir: string,
  items: SidebarItemConfig[],
  collapsed = true,
): SidebarItemConfig {
  return {
    type: 'category',
    label,
    collapsed,
    link: {type: 'doc', id: `${dir}/index`},
    items,
  };
}

function docs(dir: string, names: string[]): string[] {
  return names.map((name) => `${dir}/${name}`);
}

/**
 * Pages written by scripts/docspregen.py (platforms, frameworks) or added
 * over time (debug probes): list whatever exists, sorted by title.
 */
function listDir(dir: string): SidebarItemConfig[] {
  const abs = path.join(DOCS_DIR, dir);
  if (!fs.existsSync(abs)) {
    return [];
  }
  return fs
    .readdirSync(abs)
    .filter((f) => /\.mdx?$/.test(f) && !f.startsWith('_') && !/^index\./.test(f))
    .map((f) => {
      const content = fs.readFileSync(path.join(abs, f), 'utf8');
      const title =
        content.match(/^title:\s*"?(.+?)"?\s*$/m)?.[1] ??
        content.match(/^#\s+(.+?)(\s+\{#.*\})?\s*$/m)?.[1] ??
        f;
      return {id: `${dir}/${f.replace(/\.mdx?$/, '')}`, title};
    })
    .sort((a, b) => a.title.localeCompare(b.title, 'en', {sensitivity: 'base'}))
    .map(({id}) => id);
}

const INI = 'reference/platformio-ini';

function iniGroup(section: 'env' | 'platformio', group: string, label: string, options: string[]) {
  return {
    type: 'category' as const,
    label,
    link: {type: 'doc' as const, id: `${INI}/${section}/${group}-options`},
    items: docs(`${INI}/${section}`, options),
  };
}

function cliGroup(command: string, subcommands: string[]): SidebarItemConfig {
  const dir = `reference/cli/pio-${command}`;
  return {
    type: 'category',
    label: `pio ${command}`,
    link: {type: 'doc', id: `${dir}/index`},
    items: docs(dir, subcommands),
  };
}

const sidebars: SidebarsConfig = {
  getStarted: [
    'get-started/index',
    'get-started/what-is-platformio',
    'get-started/platformio-ide',
    'get-started/quick-start',
    section('Install PlatformIO Core', 'get-started/install', [
      'get-started/install/requirements',
      'get-started/install/installer-script',
      'get-started/install/pip',
      'get-started/install/homebrew',
      'get-started/install/shell-commands',
      'get-started/install/udev-rules',
      'get-started/install/proxy-configuration',
      'get-started/install/development-version',
      'get-started/install/integration',
      'get-started/install/uninstall',
      'get-started/install/troubleshooting',
    ]),
    'get-started/platformio-core',
    'get-started/platformio-home',
    'get-started/platformio-account',
    section('Tutorials', 'get-started/tutorials', [
      'get-started/tutorials/unit-testing-blink',
      'get-started/tutorials/espressif32/arduino-debugging-unit-testing',
      'get-started/tutorials/espressif32/espidf-debugging-unit-testing-analysis',
      'get-started/tutorials/nordicnrf52/arduino-debugging-unit-testing',
      'get-started/tutorials/nordicnrf52/zephyr-debugging-unit-testing-inspect',
      'get-started/tutorials/ststm32/stm32cube-debugging-unit-testing',
      'get-started/tutorials/riscv/riscv-asm-video-tutorial',
    ]),
  ],

  guides: [
    'guides/index',
    {
      type: 'category',
      label: 'Projects & build configuration',
      items: [
        'guides/projects/build-configurations',
        'guides/projects/examples',
      ],
    },
    section('Libraries', 'guides/libraries', [
      'guides/libraries/dependencies',
      'guides/libraries/ldf',
      'guides/libraries/creating',
    ]),
    'guides/debugging/index',
    section('Unit testing', 'guides/unit-testing', [
      section('Project structure', 'guides/unit-testing/structure', [
        'guides/unit-testing/structure/hierarchy',
        'guides/unit-testing/structure/shared-code',
        'guides/unit-testing/structure/best-practices',
      ]),
      'guides/unit-testing/runner',
      section('Testing frameworks', 'guides/unit-testing/frameworks', [
        'guides/unit-testing/frameworks/unity',
        'guides/unit-testing/frameworks/googletest',
        'guides/unit-testing/frameworks/doctest',
        section('Custom framework', 'guides/unit-testing/frameworks/custom', [
          'guides/unit-testing/frameworks/custom/runner',
          'guides/unit-testing/frameworks/custom/api',
          section('Examples', 'guides/unit-testing/frameworks/custom/examples', [
            'guides/unit-testing/frameworks/custom/examples/custom-unity-library',
          ]),
        ]),
      ]),
      section('Simulators', 'guides/unit-testing/simulators', [
        'guides/unit-testing/simulators/qemu',
        'guides/unit-testing/simulators/renode',
        'guides/unit-testing/simulators/simavr',
      ]),
      'guides/unit-testing/semihosting',
    ]),
    section('Static code analysis', 'guides/static-code-analysis', [
      section('Check tools', 'guides/static-code-analysis/tools', [
        'guides/static-code-analysis/tools/cppcheck',
        'guides/static-code-analysis/tools/clang-tidy',
      ]),
      'guides/static-code-analysis/severity',
    ]),
    'guides/remote-development',
    section('Custom platforms & boards', 'guides/custom-platforms-and-boards', [
      'guides/custom-platforms-and-boards/creating-platform',
      'guides/custom-platforms-and-boards/creating-board',
    ]),
    section('Extending the build', 'guides/scripting', [
      'guides/scripting/custom-targets',
      section('Examples', 'guides/scripting/examples', [
        'guides/scripting/examples/asking-for-input',
        'guides/scripting/examples/custom-program-name',
        'guides/scripting/examples/external-sources',
        'guides/scripting/examples/extra-linker-flags',
        'guides/scripting/examples/extra-python-packages',
        'guides/scripting/examples/override-board-configuration',
        'guides/scripting/examples/override-package-files',
        'guides/scripting/examples/platformio-ini-custom-options',
        'guides/scripting/examples/split-build-flags',
        'guides/scripting/examples/upload-to-cloud',
      ]),
    ]),
    section('IDE integrations', 'guides/ide', [
      'guides/ide/vscode',
      'guides/ide/clion',
      'guides/ide/neovim',
      'guides/ide/vim',
      'guides/ide/emacs',
      'guides/ide/sublimetext',
      'guides/ide/eclipse',
      'guides/ide/qtcreator',
      'guides/ide/visualstudio',
      'guides/ide/netbeans',
      'guides/ide/codeblocks',
      'guides/ide/cloud9',
      'guides/ide/codeanywhere',
      'guides/ide/eclipseche',
    ]),
    section('CI integrations', 'guides/ci', [
      'guides/ci/github-actions',
      'guides/ci/gitlab',
      'guides/ci/circleci',
      'guides/ci/travis',
      'guides/ci/appveyor',
      'guides/ci/drone',
      'guides/ci/shippable',
    ]),
    'guides/compile-commands',
  ],

  reference: [
    'reference/index',
    section('CLI', 'reference/cli', [
      cliGroup('access', ['grant', 'list', 'private', 'public', 'revoke']),
      cliGroup('account', [
        'destroy', 'forgot', 'login', 'logout', 'password', 'register', 'show', 'token', 'update',
      ]),
      'reference/cli/pio-boards',
      'reference/cli/pio-check',
      'reference/cli/pio-ci',
      'reference/cli/pio-debug',
      cliGroup('device', ['list', 'monitor']),
      'reference/cli/pio-home',
      cliGroup('org', ['add', 'create', 'destroy', 'list', 'remove', 'update']),
      cliGroup('pkg', [
        'exec', 'install', 'list', 'outdated', 'pack', 'publish', 'search', 'show',
        'uninstall', 'unpublish', 'update',
      ]),
      cliGroup('project', ['config', 'init', 'metadata']),
      cliGroup('remote', ['agent', 'device', 'run', 'test', 'update']),
      'reference/cli/pio-run',
      'reference/cli/pio-settings',
      {
        type: 'category',
        label: 'pio system',
        link: {type: 'doc', id: 'reference/cli/pio-system/index'},
        items: [
          section('pio system completion', 'reference/cli/pio-system/completion', [
            'reference/cli/pio-system/completion/install',
            'reference/cli/pio-system/completion/uninstall',
          ]),
          'reference/cli/pio-system/info',
          'reference/cli/pio-system/prune',
        ],
      },
      cliGroup('team', ['add', 'create', 'destroy', 'list', 'remove', 'update']),
      'reference/cli/pio-test',
      'reference/cli/pio-upgrade',
    ]),
    section('platformio.ini', INI, [
      `${INI}/interpolation`,
      section('[platformio] section', `${INI}/platformio`, [
        iniGroup('platformio', 'generic', 'Generic options', [
          'default-envs', 'description', 'extra-configs', 'name',
        ]),
        iniGroup('platformio', 'directory', 'Directory options', [
          'boards-dir', 'build-cache-dir', 'build-dir', 'cache-dir', 'core-dir', 'data-dir',
          'globallib-dir', 'include-dir', 'lib-dir', 'libdeps-dir', 'monitor-dir',
          'packages-dir', 'platforms-dir', 'shared-dir', 'src-dir', 'test-dir', 'workspace-dir',
        ]),
      ]),
      section('[env] section', `${INI}/env`, [
        iniGroup('env', 'platform', 'Platform options', [
          'platform', 'platform-packages', 'framework', 'board',
          'board-build-mcu', 'board-build-f-cpu', 'board-build-f-flash', 'board-build-flash-mode',
          'board-build-ldscript',
        ]),
        iniGroup('env', 'build', 'Build options', [
          'build-type', 'build-flags', 'build-src-flags', 'build-unflags', 'build-src-filter', 'targets',
        ]),
        iniGroup('env', 'library', 'Library options', [
          'lib-deps', 'lib-ignore', 'lib-extra-dirs', 'lib-ldf-mode', 'lib-compat-mode', 'lib-archive',
        ]),
        iniGroup('env', 'upload', 'Upload options', [
          'upload-port', 'upload-protocol', 'upload-speed', 'upload-flags', 'upload-resetmethod',
          'upload-command',
        ]),
        iniGroup('env', 'monitor', 'Monitor options', [
          'monitor-port', 'monitor-speed', 'monitor-parity', 'monitor-filters', 'monitor-rts',
          'monitor-dtr', 'monitor-eol', 'monitor-raw', 'monitor-echo', 'monitor-encoding',
        ]),
        iniGroup('env', 'check', 'Check options', [
          'check-tool', 'check-src-filters', 'check-flags', 'check-severity', 'check-skip-packages',
        ]),
        iniGroup('env', 'test', 'Test options', [
          'test-framework', 'test-filter', 'test-ignore', 'test-port', 'test-speed',
          'test-build-src', 'test-testing-command',
        ]),
        iniGroup('env', 'debug', 'Debug options', [
          'debug-tool', 'debug-test', 'debug-build-flags', 'debug-init-break', 'debug-init-cmds',
          'debug-extra-cmds', 'debug-load-cmds', 'debug-load-mode', 'debug-server', 'debug-port',
          'debug-speed', 'debug-svd-path', 'debug-server-ready-pattern',
        ]),
        iniGroup('env', 'advanced', 'Advanced options', ['extends', 'extra-scripts']),
      ]),
    ]),
    'reference/environment-variables',
    section('library.json', 'reference/library-json', [
      ...docs('reference/library-json', [
        'name', 'version', 'description', 'keywords', 'authors', 'license', 'repository',
        'homepage', 'headers', 'dependencies', 'frameworks', 'platforms', 'examples', 'scripts',
        'schema',
      ]),
      section('build', 'reference/library-json/build', docs('reference/library-json/build', [
        'flags', 'unflags', 'includedir', 'srcdir', 'srcfilter', 'extrascript', 'libarchive',
        'libldfmode', 'libcompatmode', 'builder',
      ])),
      section('export', 'reference/library-json/export', docs('reference/library-json/export', [
        'include', 'exclude',
      ])),
    ]),
    {
      type: 'category',
      label: 'Scripting API',
      items: docs('reference/scripting-api', [
        'construction-environments', 'actions', 'middlewares', 'launch-types',
      ]),
    },
  ],

  hardware: [
    'hardware/index',
    section('Platforms', 'hardware/platforms', listDir('hardware/platforms')),
    section('Frameworks', 'hardware/frameworks', listDir('hardware/frameworks')),
    'hardware/boards/index',
    {
      type: 'category',
      label: 'Debug probes',
      items: listDir('hardware/debug-probes'),
    },
  ],

  resources: [
    section('FAQ & troubleshooting', 'resources/faq', [
      'resources/faq/troubleshooting',
      'resources/faq/install-python',
      'resources/faq/arduino-vs-platformio',
      'resources/faq/ino-to-cpp',
      'resources/faq/program-memory-usage',
      'resources/faq/advanced-serial-monitor',
      'resources/faq/custom-scons-cli-options',
    ], false),
    'resources/migration',
    'resources/changelog',
  ],
};

export default sidebars;

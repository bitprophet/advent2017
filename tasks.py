from invoke import Collection, task
from invocations.pytest import test
from invocations.watch import watch


# TODO: update invocations.testing.watch_tests to take a task arg instead (it
# defaults to wrapping the non-pytest test task)
@task
def watch_tests(c, module=None, opts=None):
    """
    Watch source tree and test tree for changes, rerunning tests as necessary.

    Honors ``tests.package`` setting re: which source directory to watch for
    changes.
    """
    package = c.config.get('tests', {}).get('package')
    patterns = ['\./tests/']
    if package:
        patterns.append('\./{0}/'.format(package))
    kwargs = {'module': module, 'opts': opts}
    # Kick things off with an initial test (making sure it doesn't exit on its
    # own if tests currently fail)
    c.config.run.warn = True
    test(c, **kwargs)
    # Then watch
    watch(c, test, patterns, ['.*/\..*\.swp'], **kwargs)

ns = Collection(test, watch_tests)

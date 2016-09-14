# MIT License

# Copyright (c) 2016 Diogo Dutra

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from tests.integration.base.fixtures_model_get_related import *



class TestModelGetRelatedHard(object):
    def test_get_related_with_all_models_related_each_other(
            self, model1, model2, model3, model4,
            model5, model6, model7, model8, model9, session):
        m11 = model1(id=1)
        m12 = model1(id=2)
        m13 = model1(id=3)

        m21 = model2(id=1)
        m22 = model2(id=2)
        m23 = model2(id=3)

        m31 = model3(id=1)
        m32 = model3(id=2)
        m33 = model3(id=3)

        m41 = model4(id=1)
        m42 = model4(id=2)
        m43 = model4(id=3)

        m51 = model5(id=1)
        m52 = model5(id=2)
        m53 = model5(id=3)

        m61 = model6(id=1)
        m62 = model6(id=2)
        m63 = model6(id=3)

        m71 = model7(id=1)
        m72 = model7(id=2)
        m73 = model7(id=3)

        m81 = model8(id=1)
        m82 = model8(id=2)
        m83 = model8(id=3)

        m91 = model9(id=1)
        m92 = model9(id=2)
        m93 = model9(id=3)

        m11.model2 = m21
        m11.model3 = [m31, m32]
        m11.model4 = [m42, m43]

        m12.model2 = m22
        m12.model3 = [m33]
        m12.model4 = [m43, m41]

        m13.model2 = m23
        m13.model4 = [m41, m42]

        m21.model3 = m33
        m21.model4 = [m41, m42]
        m21.model5 = [m52, m53]

        m22.model4 = [m43]
        m22.model5 = [m51, m53]

        m23.model5 = [m51, m52]

        m31.model4 = m41
        m31.model5 = [m51, m52]
        m31.model6 = [m62, m63]

        m32.model4 = m42
        m32.model5 = [m53]
        m32.model6 = [m61, m63]

        m33.model4 = m43
        m33.model6 = [m61, m62]

        m41.model5 = m53
        m41.model6 = [m61, m62]
        m41.model7 = [m72, m73]

        m42.model6 = [m63]
        m42.model7 = [m71, m73]

        m43.model7 = [m71, m72]

        m51.model6 = m61
        m51.model7 = [m71, m72]
        m51.model8 = [m82, m83]

        m52.model6 = m62
        m52.model7 = [m73]
        m52.model8 = [m81, m83]

        m53.model6 = m63
        m53.model8 = [m81, m82]

        m61.model7 = m73
        m61.model8 = [m81, m82]
        m61.model9 = [m92, m93]

        m62.model8 = [m83]
        m62.model9 = [m91, m93]

        m63.model9 = [m91, m92]

        m71.model8 = m81
        m71.model9 = [m91, m92]

        m72.model8 = m82
        m72.model9 = [m93]

        m73.model8 = m83

        m81.model9 = m93

        session.add_all([
            m11, m12, m13, m21, m22, m33,
            m31, m32, m33, m41, m42, m43,
            m51, m52, m53, m61, m62, m63,
            m71, m72, m73, m81, m82, m83,
            m91, m92, m93
            ])
        session.commit()

        assert m11.get_related(session) == {m21, m31, m32, m42, m43}
        assert m12.get_related(session) == {m22, m33, m43, m41}
        assert m13.get_related(session) == {m23, m41, m42}

        assert m21.get_related(session) == {m11, m33, m41, m42, m52, m53}
        assert m22.get_related(session) == {m12, m43, m51, m53}
        assert m23.get_related(session) == {m13, m51, m52}

        assert m31.get_related(session) == {m11, m41, m51, m52, m62, m63}
        assert m32.get_related(session) == {m11, m42, m53, m61, m63}
        assert m33.get_related(session) == {m12, m21, m43, m61, m62}

        assert m41.get_related(session) == {m12, m13, m21, m31, m53, m61, m62, m72, m73}
        assert m42.get_related(session) == {m11, m13, m21, m32, m63, m71, m73}
        assert m43.get_related(session) == {m11, m12, m22, m33, m71, m72}

        assert m51.get_related(session) == {m22, m23, m31, m61, m71, m72, m82, m83}
        assert m52.get_related(session) == {m21, m23, m31, m62, m73, m81, m83}
        assert m53.get_related(session) == {m21, m22, m32, m41, m63, m81, m82}

        assert m61.get_related(session) == {m32, m33, m41, m51, m73, m81, m82, m92, m93}
        assert m62.get_related(session) == {m31, m33, m41, m52, m83, m91, m93}
        assert m63.get_related(session) == {m31, m32, m42, m53, m91, m92}

        assert m71.get_related(session) == {m42, m43, m51, m81, m91, m92}
        assert m72.get_related(session) == {m41, m43, m51, m82, m93}
        assert m73.get_related(session) == {m41, m42, m52, m61, m83}

        assert m81.get_related(session) == {m52, m53, m61, m71, m93}
        assert m82.get_related(session) == {m51, m53, m61, m72}
        assert m83.get_related(session) == {m51, m52, m62, m73}

        assert m91.get_related(session) == {m62, m63, m71}
        assert m92.get_related(session) == {m61, m63, m71}
        assert m93.get_related(session) == {m61, m62, m72, m81}
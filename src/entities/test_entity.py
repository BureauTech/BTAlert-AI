from entities.base import base


class TestEntity(base.Model):

    __tablename__ = 'test'
    tes_cod = base.Column(base.BigInteger, primary_key=True, autoincrement=True)
    tes_text = base.Column(base.Text, nullable=False)

    def __init__(self, tes_text: str) -> None:
        self.tes_text = tes_text

    def __repr__(self) -> str:
        return f'<TestEntity {self.tes_cod}>'
